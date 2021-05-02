$('#add-one-more').click(function () {
  var len = $('#lenData').val()
  $('#ourTable tr:last').after(`<tr id='` + ((parseInt(len) + 1).toString()) +
    `'>
    <td>
    <div class="form-groupe">
      <select name="" class="selectjs" id="selectjs-` + ((parseInt(len) + 1).toString()) +
    `">
        <option value=""></option>
      </select>
    </div>
  </td>
  <td>
    <input
      type="text"
      name="quantite-` + ((parseInt(len) + 1).toString()) +
    `"
      id="quantite-` + ((parseInt(len) + 1).toString()) +
    `"
    class='qte'
      value=""
      placeholder=""
    />
  </td>
  <td>
    <input
      type="text"
      name="unitedemeusur-` + ((parseInt(len) + 1).toString()) +
    `"
      id="unitedemeusur-` + ((parseInt(len) + 1).toString()) +
    `"
      value=""
      placeholder="..."
      disabled
    />
  </td>
  <td>
    <input
      type="text"
      name="prixunitaire-` + ((parseInt(len) + 1).toString()) +
    `"
      id="prixunitaire-` + ((parseInt(len) + 1).toString()) +
    `"
      value="19000"
      placeholder="19000"
      disabled
    />
  </td>
  <td>
    <input
      type="text"
      name="mantant-` + ((parseInt(len) + 1).toString()) +
    `"
      id="mantant-` + ((parseInt(len) + 1).toString()) +
    `"
      value="0"
      placeholder="0"
      disabled
    />
  </td>
  <td class='removeit'style='color:red'>X</td>
</tr>`);
  var lista = []

  var $eventSelect = $("#selectjs-" + ((parseInt(len) + 1).toString()))
  $eventSelect.select2({
    placeholder: "Type",
    ajax: {
      type: "GET",

      dataType: 'json',
      url: function (params) {
        return 'loadMore/' + params.term;
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




  $eventSelect.on("select2:close", function (e) {
    var num = ($(this).parents()[2].id)

    var pos = lista.map(function (e) {

      return e.nom_article;
    }).indexOf($(`#select2-selectjs-` + num + `-container`).text());
    $('#unitedemeusur-' + num).val(lista[pos]['unite_mesure'])

  })

  $('#lenData').val((parseInt(len) + 1).toString())
})

$('#ourTable').on('click', '.removeit', function () {
  $(this).parent().remove();
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
  $('#MHT').val(mht.toString())






})