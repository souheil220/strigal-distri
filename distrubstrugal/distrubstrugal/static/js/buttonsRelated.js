$('#add-one-more').click(function () {
  var len = $('#lenData').val()
  console.log(len)

  $('#myRow-' + len).after(`
    <div id='myRow-` + ((parseInt(len) + 1).toString()) + `' class="row align-items-end col-sm-12 test" style="margin-bottom: 3%;">
      <div class="col col-12 col-lg-3 col-xl-3">
          <div class="text-center d-lg-none">Article</div>
          <div class="">
            <select name="article-` + ((parseInt(len) + 1).toString()) + `" class="form-control valodo" id="selectjs-` + ((parseInt(len) + 1).toString()) + `-1" required>
              <option value=""></option>
            </select>
          </div>
      </div>
      
      <div class="col col-12 col-lg-3 col-xl-3 ">
        <div class="text-center d-lg-none">ref Article</div>
        <div class="">
            <select class="form-control valodo" id="selectjs-` + ((parseInt(len) + 1).toString()) + `-2" required>
              <option value=""></option>
            </select>
        </div>
      </div>

      <div class="col col-12 col-lg-1 col-xl-1">
      <div class="text-center d-lg-none">Conditionement</div>
      <div class="">
        <input
          type="text"
          name="conditionnement-` + ((parseInt(len) + 1).toString()) + `"
          id="conditionnement-` + ((parseInt(len) + 1).toString()) + `"
          value=""
          placeholder="..."
          readonly
        />
      </div>
    </div>

      <div class="col col-12 col-lg-1 col-xl-1">
        <div class="text-center d-lg-none">Quantité</div>
          <div class="">
            <input
              type="text"
              name="quantite-` + ((parseInt(len) + 1).toString()) + `"
              id="quantite-` + ((parseInt(len) + 1).toString()) + `"
              class="qte valodo"
              placeholder="0"
              required='true'
            />
          </div>
      </div>

      <div class="col col-12 col-lg-1 col-xl-1">
          <div class="text-center d-lg-none">Unité de mesure</div>
          <div class="">
            <input
              type="text"
              name="unitedemeusur-` + ((parseInt(len) + 1).toString()) + `"
              id="unitedemeusur-` + ((parseInt(len) + 1).toString()) + `"
              value=""
              placeholder="..."
              readonly
            />
          </div>
      </div>


      <div class="col col-12 col-lg-1 col-xl-1">
          <div class="text-center d-lg-none">Prix Unitaire</div>
          <div class="">
            <input
              type="text"
              name="prix_unitaire-` + ((parseInt(len) + 1).toString()) + `"
              id="prix_unitaire-` + ((parseInt(len) + 1).toString()) + `"
              value=""
              placeholder=""
              readonly
            />
          </div>
      </div>

      <div class="col col-12 col-lg-1 col-xl-1" >
          <div class="text-center d-lg-none">Montant</div>
          <div class="">
              <input
                hidden
                type="text"
                name="mantant-` + ((parseInt(len) + 1).toString()) + `"
                id="mantant-` + ((parseInt(len) + 1).toString()) + `"
                value="0"
                placeholder="0"
                readonly
              />
              <input
                type="text"
                name="mantant-` + ((parseInt(len) + 1).toString()) + `-forshow"
                id="mantant-` + ((parseInt(len) + 1).toString()) + `-forshow"
                value="0"
                placeholder="0"
                readonly
              />
          </div>
      </div>

      <div class="col col-12 col-lg-1 col-xl-1 text-center">
        <p class='removeit button icon solid fa-trash' 
          style=" margin:0;color:#af1010 !important; margin-right:15px; box-shadow: inset 0 0 0 2px #eeeeee !important">
        </p>
      </div>
    </div>`)
  var lista = []

  var $eventSelect = $("#selectjs-" + ((parseInt(len) + 1).toString()) + "-1")
  $eventSelect.select2({
    placeholder: "Type",
    ajax: {
      type: "GET",

      dataType: 'json',
      url: function (params) {
        console.log($(this)[0].id)
        var num = $(this)[0].id
        var whiche = num.substring(num.length - 1)
        var pathname = window.location.pathname;
        pathname === '/' ? loca = 'distributeur/loadMore/' + params.term + "/" + whiche :
          loca = 'loadMore/' + params.term + "/" + whiche
        return loca
      },

      processResults: function (data) {

        lista = []
        for (d in data) {
          lista.push(data[d])
        }
        console.log(lista)
        var fin = []
        fin = data

        return {


          results: $.map(fin, function (item) {
            console.log(item.nom_article)
            $eventSelect.on("select2:select", function (e) {
              id = e.params.data.id
              var $newOption = $("<option selected='selected'></option>").val(id).text(id)

              $("#selectjs-" + ((parseInt(len) + 1).toString()) + "-2").append($newOption).trigger('change');
            })
            return {
              text: item.nom_article,
              id: item.id_article

            }
          })
        }


      },
      cache: true,


    }
  })


  var $eventSelect2 = $("#selectjs-" + ((parseInt(len) + 1).toString()) + "-2")
  $eventSelect2.select2({
    placeholder: "Type",
    ajax: {
      type: "GET",

      dataType: 'json',
      url: function (params) {
        var num = $(this)["context"].id
        console.log(num)
        var whiche = num.substring(num.length - 1)
        var pathname = window.location.pathname;
        pathname === '/' ? loca = 'distributeur/loadMore/' + params.term + "/" + whiche :
          loca = 'loadMore/' + params.term + "/" + whiche
        return loca
      },

      processResults: function (data) {
        // console.log(data)
        lista = []
        for (d in data) {
          lista.push(data[d])
        }
        // console.log(lista)
        var fin = []
        fin = data

        return {


          results: $.map(fin, function (item) {
              // console.log(item)

              $eventSelect2.on("select2:select", function (e) {
                nom = e.params.data.id
                valeur = e.params.data.text
                var $newOption = $("<option selected='selected'></option>").val(valeur).text(nom)

                $("#selectjs-" + ((parseInt(len) + 1).toString()) + "-1").append($newOption).trigger('change');
              })

              return {
                text: item.id_article,
                id: item.nom_article

              }

            }

          )

        }



      },
      cache: true,


    }
  })

  function closeSelect(idContainer, e, that) {

    console.log(that.parents()[2].id)

    var num = (that.parents()[2].id)
    console.log("that  " + num)
    var aa = num.lastIndexOf("-") + 1
    var bb = num.lastIndexOf(num.substr(num.length - 1)) + 1
    num = num.substring(
      aa,
      bb
    );

    console.log("num " + num)
    var pos = lista.map(function (event) {
      if (idContainer === "#select2-selectjs-" + num + "-1-container") {
        return event.nom_article
      } else {
        return event.id_article
      }



    }).indexOf($(idContainer).text());
    console.log(lista[pos]['conditionnement'])

    $('#unitedemeusur-' + num).val(lista[pos]['unite_mesure'])
    $('#conditionnement-' + num).val(lista[pos]['conditionnement'])
    $('#prix_unitaire-' + num).val(lista[pos]['prix_unitaire'])

    console.log("select2:close", e);
  }



  $eventSelect.on("select2:close", function (e) {
    var num = ($(this).parents()[2].id)
    var aa = num.lastIndexOf("-") + 1
    var bb = num.lastIndexOf(num.substr(num.length - 1)) + 1
    num = num.substring(
      aa,
      bb
    );
    closeSelect("#select2-selectjs-" + num + "-1-container", e, $(this))
  })

  $eventSelect2.on("select2:close", function (e) {
    var num = ($(this).parents()[2].id)
    var aa = num.lastIndexOf("-") + 1
    var bb = num.lastIndexOf(num.substr(num.length - 1)) + 1
    num = num.substring(
      aa,
      bb
    );
    closeSelect("#select2-selectjs-" + num + "-2-container", e, $(this))
  })

  $('#lenData').val((parseInt(len) + 1).toString())
})

function intspace(params) {
  if (params.toString().indexOf('.') === -1) {
    return params.toLocaleString()
  } else {

    params = params.toLocaleString()
    return params
  }
}


$("body").on('click', '.removeit', function () {

  console.log($(this).parent().parent())
  $(this).parent().parent().remove();
  var len = $('#lenData').val()
  $('#lenData').val((parseInt(len) - 1).toString())
  var lenData = parseInt($('#lenData').val())

  var mht = 0


  console.log($('#lenData').val())

  for (var i = 1; i <= lenData; i++) {
    console.log(i)
    console.log($('#mantant-' + i).val())
    mht = mht + parseInt($('#mantant-' + i).val())
    console.log(mht)

  }
  $('#MHT-forshow').val(intspace(mht))
  $('#MHT').val(mht.toString())






})