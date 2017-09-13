// advanced search options
// function cleanForm($form) {
//     $form.find('input:text, input:password, input:file, select, textarea').val('');
//     $form.find('input:radio, input:checkbox').removeAttr('checked').removeAttr('selected');
// }

function clearForm(element) {
    $(element).find(':input').each(function () {
        switch (this.type) {
            case 'password':
            case 'select-multiple':
            case 'select-one':
            case 'text':
            case 'textarea':
                $(this).val('');
                break;
            case 'checkbox':
            case 'radio':
                this.checked = false;
        }
    });
}

function toggleAdvancedSearch() {
    if (jQuery("#advanced-search-enabled").val() != "1") {
        jQuery("#advanced-search-enabled").val("1");
        jQuery("#advanced-search-control").html("<i class=\"fa fa-minus\">");
    } else {
        var query = jQuery("#id_q").val();
        jQuery("#advanced-search-enabled").val("0");
        jQuery("#advanced-search-control").html("<i class=\"fa fa-plus\">");
        clearForm(jQuery("#search"));
        jQuery("#id_q").val(query);
    }
    jQuery("#advanced-search").toggle()
}
