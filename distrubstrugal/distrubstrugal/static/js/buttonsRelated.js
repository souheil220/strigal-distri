$('#add-one-more').click(function () {
  var len = $('#lenData').val()
  $('#ourTable tr:last').after(`<tr id='td_num-` + ((parseInt(len) + 1).toString()) +
    `'>
  <td>
    <select onChange = "selectChange('#demo-category-` + ((parseInt(len) + 1).toString()) + `')" name="demo-category-` + ((parseInt(len) + 1).toString()) +
    `" id="demo-category-` + ((parseInt(len) + 1).toString()) +
    `">
      <option value="">- Article -</option>
      <option value="1">Manufacturing</option>
      <option value="1">Shipping</option>
      <option value="1">Administration</option>
      <option value="1">Human Resources</option>
    </select>
  </td>
  <td>
    <input
      type="text"
      name="description-` + ((parseInt(len) + 1).toString()) +
    `"
      id="description-` + ((parseInt(len) + 1).toString()) +
    `"
      value=""
      placeholder="..."
      disabled
    />
  </td>
  <td>
    <input
      type="text"
      name="quantite-` + ((parseInt(len) + 1).toString()) +
    `"
      id="quantite-` + ((parseInt(len) + 1).toString()) +
    `"
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
      value=""
      placeholder="..."
      disabled
    />
  </td>
  <td>
    <input
      type="text"
      name="tax-` + ((parseInt(len) + 1).toString()) +
    `"
      id="tax-` + ((parseInt(len) + 1).toString()) +
    `"
      value=""
      placeholder="..."
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