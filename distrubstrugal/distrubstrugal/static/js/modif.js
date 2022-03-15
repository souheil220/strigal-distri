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



//Liste des prix
try {
    var $eventSelectLP = $('select.select2LP')
    $eventSelectLP.select2({
        placeholder: "Recherche List Des Prix",
        ajax: {
            type: "GET",
            dataType: 'json',
            url: function (params) {
                var whicheone = 'listP'
                console.log(window.location.pathname)
                return window.location.origin + '/commerciale/loadMoreD/' + params.term + '/' + whicheone
                return window.location.origin
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
                        return {
                            text: item.nom_list_prix,
                            id: item.id_list_prix
                        }
                    })
                }
            },
            cache: true,
        }
    })
} catch (error) {
    console.log(error)
}


//Creer Facture
try {
    var $eventSelectCF = $('select.select2CF')
    $eventSelectCF.select2({
        placeholder: "Recherche Creer Facture",
        ajax: {
            type: "GET",
            dataType: 'json',
            url: function (params) {
                var whicheone = 'creerF'
                console.log(window.location.pathname)
                return window.location.origin + '/commerciale/loadMoreD/' + params.term + '/' + whicheone
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
                        return {
                            text: item.policy_creer_facture,
                            id: item.id_creer_facture
                        }
                    })
                }
            },
            cache: true,
        }
    })
} catch (error) {
    console.log(error)
}


//Vendeur
try {
    var $eventSelectV = $('select.select2V')
    $eventSelectV.select2({
        placeholder: "Recherche Vendeur",
        ajax: {
            type: "GET",
            dataType: 'json',
            url: function (params) {
                var whicheone = 'vendeur'
                console.log(window.location.pathname)
                return window.location.origin + '/commerciale/loadMoreD/' + params.term + '/' + whicheone
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
                        return {
                            text: item.name_vendeur,
                            id: item.id_vendeur
                        }
                    })
                }
            },
            cache: true,
        }
    })
} catch (error) {
    console.log(error)
}


//Equipe Commerciale
try {
    var $eventSelectEC = $('select.select2EC')
    $eventSelectEC.select2({
        placeholder: "Recherche Equipe Commerciale",
        ajax: {
            type: "GET",
            dataType: 'json',
            url: function (params) {
                var whicheone = 'equipeC'
                console.log(window.location.pathname)
                return window.location.origin + '/commerciale/loadMoreD/' + params.term + '/' + whicheone
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
                        return {
                            text: item.name_equipe,
                            id: item.id_equipe
                        }
                    })
                }
            },
            cache: true,
        }
    })
} catch (error) {
    console.log(error)
}


//Régime Fiscal
try {
    var $eventSelectRF = $('select.select2RF')
    $eventSelectRF.select2({
        placeholder: "Recherche Régime Fiscal",
        ajax: {
            type: "GET",
            dataType: 'json',
            url: function (params) {
                var whicheone = 'regimeF'
                console.log(window.location.pathname)
                return window.location.origin + '/commerciale/loadMoreD/' + params.term + '/' + whicheone
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

                        return {
                            text: item.nom_regime_fiscal,
                            id: item.id_regime_fiscal
                        }
                    })
                }
            },
            cache: true,
        }
    })
} catch (error) {
    console.log(error)
}

function checkIfAllRequirement() {
    if ($('#selectjsLP-1-1').children('option').length <= 0) {
        $("#approuver").prop("disabled", true);
        return
    }
    if ($('#selectjsRF-1-1').children('option').length <= 0) {
        $("#approuver").prop("disabled", true);
        return
    }
    if ($('#selectjsCF-1-1').children('option').length <= 0) {
        $("#approuver").prop("disabled", true);
        return
    }
    if ($('#selectjsEC-1-1').children('option').length <= 0) {
        $("#approuver").prop("disabled", true);
        return
    }
    if ($('#selectjsV-1-1').children('option').length <= 0) {
        $("#approuver").prop("disabled", true);
        return
    }
    if (checkIfQTEisRed()) {
        $("#approuver").prop("disabled", true);
        return
    }

    $("#approuver").prop("disabled", false);
}


function checkIfQTEisRed() {
    red = false
    var datalength = $('#lenData').val()
    for (i = 1; i <= datalength; i++) {
        if ($(`#quantite-${i}`).css("color") == 'rgb(255, 0, 0)') {
            red = true
            break
        }
    }
    return red
}

$eventSelectLP.on("select2:close", function (e) {
    checkIfAllRequirement()
})
$eventSelectRF.on("select2:close", function (e) {
    checkIfAllRequirement()
})
$eventSelectCF.on("select2:close", function (e) {
    checkIfAllRequirement()
})
$eventSelectEC.on("select2:close", function (e) {
    checkIfAllRequirement()
})
$eventSelectV.on("select2:close", function (e) {
    checkIfAllRequirement()
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

$("body").on("keyup", '.qteDetail', function () {
    var lenData = parseInt($('#lenData').val())
    var mht = 0
    var num = ($(this)[0].id)
    var aa = num.lastIndexOf("-") + 1
    var bb = num.lastIndexOf(num.substr(num.length - 1)) + 1
    num = num.substring(
        aa,
        bb
    );


    if ($('#quantite-' + num).val().length > 0 && $('#quantite-' + num).val() !== '0') {

        if ((parseFloat($('#quantite-' + num).val()) % parseFloat($('#conditionnement-' + num).val())) != 0) {
            $('#quantite-' + num).css('color', 'red');
        } else {
            console.log("cahnged")
            $('#quantite-' + num).css('color', 'black');
        }

        var montant = (parseFloat($('#quantite-' + num).val()) * parseFloat($('#prix_unitaire-' + num).val()))


        $('#mantant-' + num).val(montant.toString())

        calculerRemise(num)
    } else {

        $('#mantant-' + num).val('0')
    }


    // for (var i = 1; i <= lenData; i++) {

    //     mht = mht + parseFloat($('#mantant-' + i).val())

    // }



    // $('#MHT').val(mht)
    // $('#MHT-forshow').val(intspace(mht))

    checkIfAllRequirement()

})

$("body").on("keyup", '.discount', function () {




    var num = ($(this)[0].id)
    var aa = num.lastIndexOf("-") + 1
    var bb = num.lastIndexOf(num.substr(num.length - 1)) + 1
    num = num.substring(
        aa,
        bb
    );
    calculerRemise(num)



})

function calculerRemise(num) {

    var remise = parseFloat($('#remise-' + num).val())


    if ($('#remise-' + num).val() === "") {
        remise = 0
        console.log("remise " + remise)
    }

    console.log("remise " + remise)

    console.log()

    var remiseTotal = 0

    if ($('#remise-' + num).val().length >= 0) {

        remiseTotal = remiseTotal + (parseFloat($('#quantite-' + num).val()) * parseFloat($('#prix_unitaire-' + num).val()) * remise / 100)
        console.log(remiseTotal)

        $('#remiseTotaleLigne-' + num).val(remiseTotal.toString())

        $("#remiseTotal").val(calculerTotalRemise().toString())
        console.log("htRemise " + calculerTotalRemise())
        var htRemise = calculerTotalRemise()
        finalHT = parseFloat($("#mat").val()) - htRemise
        $("#MHT-forshow").val(finalHT.toString())
        $("#MHT").val(finalHT.toString())
    } else {

        $('#remiseTotal').val('0')
    }

}

function calculerTotalRemise() {
    var lenData = parseInt($('#lenData').val())
    var totaleRemise = 0
    for (var i = 1; i < lenData + 1; i++) {
        totaleRemise = totaleRemise + parseFloat($(`#remiseTotaleLigne-${i}`).val())
    }
    return totaleRemise
}