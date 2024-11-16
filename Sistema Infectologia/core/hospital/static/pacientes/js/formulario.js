$(function () {
    $('#fecha_nacimiento').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'es',
    });

    $('.select2').select2({
        theme: 'bootstrap4',
        language: "es"
    });
});