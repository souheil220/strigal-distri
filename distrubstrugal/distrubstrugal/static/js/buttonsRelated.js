$('#add-one-more').click(function () {
  var len = $('#lenData').val()
  $('#ourTable tr:last').after(`<tr id='td_num-` + ((parseInt(len) + 1).toString()) +
    `'>
  <td>
  <div class="div-filter">
  <div class="filer-ids">
      <input autocomplete="off" id="filtrer-` + ((parseInt(len) + 1).toString()) + `" name="ids" class="chosen-value chosen-value-` + ((parseInt(len) + 1).toString()) + `" type="text" placeholder="Type to filter">
      <div style="position:relative">
          <ul class="value-list test-` + ((parseInt(len) + 1).toString()) + `">
          </ul>
      </div>
  </div>
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
      value=""
      placeholder="..."
      disabled
    />
  </td>
  <td class='removeit'style='color:red'>X</td>
</tr>`);
  $('#lenData').val((parseInt(len) + 1).toString())
})

$('#ourTable').on('click', '.removeit', function () {
  $(this).parent().remove();
  var len = $('#lenData').val()
  $('#lenData').val((parseInt(len) - 1).toString())
})