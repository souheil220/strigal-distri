var $eventSelect = $('select.select2A')
$eventSelect.select2({
    placeholder: "Type",
    ajax: {
        type: "GET",

        dataType: 'json',
        url: function (params) {
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
            var fin = []
            fin = data

            return {


                results: $.map(fin, function (item) {
                    $eventSelect.on("select2:select", function (e) {
                        id = e.params.data.id
                        var $newOption = $("<option selected='selected'></option>").val(id).text(id)
                        var num = ($(this)['context'].name)
                        num = (num.substr(num.length - 1))
                        console.log($newOption)
                        $("#selectjs-" + num + "-2").append($newOption).trigger('change');
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

var $eventSelect2 = $("select.select2C")
$eventSelect2.select2({
    placeholder: "Type",
    ajax: {
        type: "GET",

        dataType: 'json',
        url: function (params) {
            var num = $(this)["context"].id
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
                            var num = ($(this)['context'].name)
                            num = (num.substr(num.length - 1))
                            var $newOption = $("<option selected='selected'></option>").val(valeur).text(nom)

                            $("#selectjs-" + num + "-1").append($newOption).trigger('change');
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
    var num = that['context'].name
    num = num.substr(num.length - 1)
    var pos = lista.map(function (event) {
        if (idContainer === "#select2-selectjs-" + num + "-1-container") {
            return event.nom_article
        } else {
            return event.id_article
        }
    }).indexOf($(idContainer).text());


    $('#unitedemeusur-' + num).val(lista[pos]['unite_mesure'])
    $('#prix_unitaire-' + num).val(lista[pos]['prix_unitaire'])

}

$eventSelect.on("select2:close", function (e) {
    var num = ($(this)['context'].name)
    num = (num.substr(num.length - 1))

    closeSelect("#select2-selectjs-" + num + "-1-container", e, $(this))
    $('#prix_unitaire-' + num).change(function () {
        calculate(num)
    });


    $('#prix_unitaire-' + num).trigger('change');
})

$eventSelect2.on("select2:close", function (e) {
    var num = ($(this)['context'].name)
    num = (num.substr(num.length - 1))
    closeSelect("#select2-selectjs-" + num + "-2-container", e, $(this))
    $('#prix_unitaire-' + num).change(function () {
        calculate(num)
    });


    $('#prix_unitaire-' + num).trigger('change');
})


function calculate(num) {
    var lenData = parseInt($('#lenData').val())
    var mht = 0


    if ($('#quantite-' + num).val().length > 0 && $('#quantite-' + num).val() !== '0') {

        var montant = (parseInt($('#quantite-' + num).val()) * parseInt($('#prix_unitaire-' + num).val()))


        $('#mantant-' + num).val(montant.toString())
        $('#mantant-' + num + "-forshow").val(intspace(montant))
    } else {

        $('#mantant-' + num).val('0')
    }


    for (var i = 1; i <= lenData; i++) {

        mht = mht + parseInt($('#mantant-' + i).val())

    }



    $('#MHT').val(mht)
    $('#MHT-forshow').val(intspace(mht))


}