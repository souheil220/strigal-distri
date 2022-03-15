import psycopg2
from psycopg2 import Error
import datetime


class SQLConnexion:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connection(self):
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
            return [cursor, connection]

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def closeConnection(self, cursor, connection):
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    def insert_sale_order(self, cursor, connection, user_email, ref_description, name, order_date, distributeur_id, total, regime_fiscal, price_list_id, equipe_commercial_id, creer_facture, payment_on_picking, warehouse_id):
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        concatenated_date = str(current_date)+' '+str(current_time)

        print("the date ", type(concatenated_date))
        commercial_id = self.get_commercial_id(cursor, user_email)
        # date_order = datetime.strptime(order_date, '%d/%m/%y %H:%M:%S')
        amount_taxed = total * 19/100
        amount_untaxed = total - amount_taxed
        company_id = 19
        _ruid = str(commercial_id) + "_" + str(round(datetime.datetime.now().timestamp())
                                               ) + "_" + str(self.getLastId(cursor, 'public.sale_order') + 1)

        sqlQuery = '''
            INSERT INTO public.sale_order
            (origin, create_date, write_uid, client_order_ref, date_order, partner_id, amount_tax, 
            procurement_group_id, fiscal_position, amount_untaxed, payment_term, message_last_post, 
            company_id, note, state, pricelist_id, create_uid, section_id, write_date, 
            partner_invoice_id, user_id, date_confirm, amount_total, project_id, "name", 
            partner_shipping_id, order_policy, campaign_id, medium_id, source_id, crm_project_id, 
            fiscal_stamp_amount, fiscal_stamp, date_validite, "_ruid", parent_partner_id, company_parent_id, 
            picking_policy, incoterm, warehouse_id, shipped, condition_livraison_id, payment_on_picking,
             journal_id, matricule, date_out, date_in, driver, transporter, matricule_remorque, enlevement)
            VALUES(
                {}, (TIMESTAMP '{}'), '{}', '{}', (TIMESTAMP '{}'), {}, {}, 
                {}, {}, {}, {}, {}, 
                {}, {}, '{}', {}, {}, {}, (TIMESTAMP '{}'), 
                {}, {}, {}, {}, {}, '{}', 
                {}, '{}', {}, {}, {}, {}, 
                {}, {}, {}, '{}', {}, {},
                '{}', {}, {}, {}, {}, {}, 
                {}, {}, {}, {}, {}, {}, {}, {}) RETURNING id;
        '''.format("''", self.get_det_time(), commercial_id, ref_description, order_date, distributeur_id, amount_taxed,
                   "NULL", regime_fiscal, amount_untaxed, "NULL", "NULL",
                   company_id, "''", 'draft', price_list_id, commercial_id, equipe_commercial_id, order_date,
                   distributeur_id, commercial_id, "NULL", total, "NULL", name,
                   distributeur_id, creer_facture, "NULL", "NULL", "NULL", "NULL",
                   0, False, "NULL", _ruid, distributeur_id, company_id,
                   "direct", "NULL", warehouse_id, False, "NULL", payment_on_picking,
                   "NULL", "''", "NULL", "NULL", "''", "''", "''", "''")

        print(sqlQuery)

        # record_to_insert = ('', concatenated_date, commercial_id, ref_description, order_date, distributeur_id, amount_taxed,
        #                     0, regime_fiscal, amount_untaxed, 0, '',
        #                     company_id, '', 'draft', price_list_id, commercial_id, equipe_commercial_id, order_date,
        #                     distributeur_id, commercial_id, '', total, 0, ref_description,
        #                     distributeur_id, creer_facture, 0, 0, 0, 0,
        #                     0, False, '', _ruid, distributeur_id, company_id,
        #                     'direct', 0, warehouse_id, False, 0, payment_on_picking,
        #                     0, '', '', '', '', '', '', '')
        try:
            cursor.execute(sqlQuery)
            connection.commit()
            id_of_new_row = cursor.fetchone()[0]
            print(id_of_new_row)
            return id_of_new_row
        except (Exception, Error) as error:
            print("I couldn't insert because ", error)

    def insert_sale_order_line(self, cursor, connection, user_email, quantity, unite_de_meusure, sequence, price_unit, product_name, default_code_product, id_distributeur, id_commande, discount, product_id, conditionnement):
        commercial_id = self.get_commercial_id(cursor, user_email)
        company_id = 19
        qty_conditionnee = quantity / conditionnement
        _ruid = str(commercial_id) + "_" + str(round(datetime.datetime.now().timestamp())
                                               ) + "_" + str(self.getLastId(cursor, 'public.sale_order_line') + 1)

        unite_de_mesure = self.get_product_uom(cursor, unite_de_meusure)
        sqlQuery = '''
        INSERT INTO public.sale_order_line
        (product_uos_qty,create_date,product_uom,sequence,price_unit,
         product_uom_qty,write_uid,product_uos,invoiced,create_uid,
         company_id,name,delay,state,order_partner_id,
         order_id,discount,write_date,product_id,salesman_id,
         th_weight,address_allotment_id,qty_conditionnee,product_packaging,available,
         kit_line_id,order_uom_qty,order_qty_conditionnee,_ruid,route_id,
         analytic_account_id,epaisseur,largeur,order_nb_item,
         nb_item,longueur,crm_project_id)
         VALUES(
             {},(TIMESTAMP '{}'),{},{},{},
             {},{},{},{},{},
             {},'{}',{},'{}',{},
             {},{},(TIMESTAMP '{}'),{},{},
             {},{},{},{},{},
             {},{},{},'{}',{},
             {},{},{},{},
             {},{},{}
         ) RETURNING id
        '''.format(quantity, self.get_det_time(), unite_de_mesure, sequence, price_unit,
                   quantity, commercial_id, unite_de_mesure, False, commercial_id,
                   company_id, product_name, 0, "draft", id_distributeur,
                   id_commande, discount, self.get_det_time(), product_id, id_distributeur,
                   self.get_th_weight(
                       cursor, quantity, default_code_product), "NULL", qty_conditionnee, "NULL", True,
                   "NULL", quantity, qty_conditionnee, _ruid, "NULL",
                   "NULL", 0, 0, 0,
                   0, 0, "NULL")
        print(sqlQuery)
        try:
            cursor.execute(sqlQuery)
            connection.commit()
        except (Exception, Error) as error:
            print("I couldn't insert because ", error)

    def get_commercial_id(self, cursor, user_email):
        sqlQuery = "SELECT id FROM public.res_users WHERE login = {}".format(
            "'kamel.laouari@strugal-dz.com'")
        print(sqlQuery)
        cursor.execute(sqlQuery)
        id_commercial = cursor.fetchone()
        return id_commercial[0]

    def getLastId(self, cursor, table):
        sqlQuery = "SELECT id FROM {} ORDER BY id DESC LIMIT 1".format(table)
        cursor.execute(sqlQuery)
        id = cursor.fetchone()
        return id[0]

    def get_product_uom(self, cursor, unite_de_meusure):
        sqlQuery = "select id from public.product_uom where name='{}'".format(
            unite_de_meusure)
        cursor.execute(sqlQuery)
        unity = cursor.fetchone()
        return unity[0]

    def get_th_weight(self, cursor, quantity, default_code):
        sqlQuery = "select weight from public.product_template where template_code='{}'".format(
            default_code)
        print(sqlQuery)
        cursor.execute(sqlQuery)
        if(cursor.fetchone() is not None):
            weight = cursor.fetchone()[0]
            th_weight = weight*quantity
            return th_weight
        else:
            return 0

    def get_det_time(self):
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        concatenated_date = str(current_date)+' '+str(current_time)
        return concatenated_date

    def get_num_sequence(self, cursor, company_id, warehouse_id):

        sqlQuery = "select number_next ,prefix from ir_sequence where company_id ={} and warehouse_id ={} and code = 'sale.order'".format(
            company_id, warehouse_id)

        print(sqlQuery)
        cursor.execute(sqlQuery)
        num_sequence = cursor.fetchone()
        return num_sequence

    def update_num_sequence(self, cursor, connection, number, company_id, warehouse_id):
        sqlQuery = "UPDATE ir_sequence SET number_next = {} where company_id ={} and warehouse_id ={} and code = 'sale.order'".format(
            number, company_id, warehouse_id)

        cursor.execute(sqlQuery)
        connection.commit()

    def get_articles(self, cursor):
        sqlQuery = '''
        select id,name_template,default_code,name,qty,lst_price,id_154_sur_char, id_346_sur_char,id_347_sur_char,id_376_sur_char,
						
						id_154_prix_par_list, id_346_prix_par_list,id_347_prix_par_list,id_376_prix_par_list
        from ( 
        (select pp.id,default_code, name_template, pu.name,qty,pp.lst_price from product_product as pp
                    inner join product_template as pt
                    on pp.product_tmpl_id = pt.id 
                    inner join product_uom as pu 
                    on pu.id = pt.uom_id 
                    inner join product_packaging as pp2 
                    on pp2.product_tmpl_id = pt.id 
                    where pt.company_id = 19
                    and pt.sale_ok = true 
                    and pt.active = true 
                    ) as baar 
            inner join 
            
        (select * from crosstab ('SELECT
        product_product.id,
        product_pricelist.name,
        product_pricelist_item.price_surcharge

        FROM
        public.product_pricelist_item inner join public.product_pricelist_version on product_pricelist_item.price_version_id = product_pricelist_version.id
        inner join  public.product_pricelist on product_pricelist_version.pricelist_id = product_pricelist.id inner join  public.product_product on
        product_pricelist_item.product_id = product_product.id
        
        where
        product_pricelist.id in (154,346,347,376)
        and product_pricelist_version.active=''True'' 
        and (CASE
            WHEN date_end is null THEN date_end is null
            ELSE date_end > CURRENT_DATE
            END) order by 1,2')
        as ct(product_id int,id_154_sur_char numeric,id_346_sur_char numeric, id_347_sur_char numeric,id_376_sur_char numeric )) as foo 
        
        on foo.product_id = baar.id
        
        inner join 
        
        
        (select * from crosstab ('SELECT
        product_product.id,
        product_pricelist.name,
        product_product.lst_price
        FROM
        public.product_pricelist_item inner join public.product_pricelist_version on product_pricelist_item.price_version_id = product_pricelist_version.id
        inner join  public.product_pricelist on product_pricelist_version.pricelist_id = product_pricelist.id inner join  public.product_product on
        product_pricelist_item.product_id = product_product.id
        
        where
        product_pricelist.id in (154,346,347,376)
        and product_pricelist_version.active=''True'' 
        and (CASE
            WHEN date_end is null THEN date_end is null
            ELSE date_end > CURRENT_DATE
            END) order by 1,2')
        as ct(product_id int,id_154_ls_list numeric, id_346_ls_list numeric,id_34_ls_list numeric,id_376_ls_list numeric )) as boo 
        on foo.product_id = boo.product_id
        inner join 
        
        (select * from crosstab ('SELECT
        product_product.id,
        product_pricelist.name,
        (product_product.lst_price+product_pricelist_item.price_surcharge)
        FROM
        public.product_pricelist_item inner join public.product_pricelist_version on product_pricelist_item.price_version_id = product_pricelist_version.id
        inner join  public.product_pricelist on product_pricelist_version.pricelist_id = product_pricelist.id inner join  public.product_product on
        product_pricelist_item.product_id = product_product.id
        
        where
        product_pricelist.id in (154,346,347,376)
        and product_pricelist_version.active=''True'' 
        and (CASE
            WHEN date_end is null THEN date_end is null
            ELSE date_end > CURRENT_DATE
            END) order by 1,2')

        as ct(product_id int,id_154_prix_par_list numeric, id_346_prix_par_list numeric,id_347_prix_par_list numeric,id_376_prix_par_list numeric ) ) as test 
        on foo.product_id = test.product_id
        )
        '''

        cursor.execute(sqlQuery)
        data = cursor.fetchall()
        return data
