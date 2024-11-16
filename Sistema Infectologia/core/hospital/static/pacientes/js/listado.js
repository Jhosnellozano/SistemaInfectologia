let data_list = null;
$(function () {
    data_list = $('#data_list').DataTable({
        responsive: false,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search'
            },
            dataSrc: ""
        },
        language: {
            decimal: "",
            sLengthMenu: "Mostrar _MENU_ registros",
            emptyTable: "No hay información",
            info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            infoEmpty: "Mostrando 0 a 0 de 0 Entradas",
            infoFiltered: "(Filtrado de _MAX_ total entradas)",
            infoPostFix: "",
            thousands: ",",
            lengthMenu: "Mostrar _MENU_ Entradas",
            loadingRecords: "Cargando...",
            processing: "Procesando...",
            searchPlaceholder: "Buscar",
            search: "",
            zeroRecords: "Sin resultados encontrados",
            paginate: {
            first: "Primero",
            last: "Ultimo",
            next: "<span class='fa fa-angle-double-right'></span>",
            previous: "<span class='fa fa-angle-double-left'></span>",
            },
            buttons: {
            copy: "Copiar", 
            print: "Imprimir",
            },
        },        
        columns: [
            {"data": "full_name"},
            {"data": "cedula"},
            {"data": "fecha_nacimiento"},
            {"data": "edad"},
            {"data": "sexo.label", className: "text-center"},
            {"data": "telefono"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [1],
                class: 'text-center',
                orderable: true,
                render: function (data, type, row) {
                    return `${row.tipo_cedula.value}-${row.cedula}`
                }
            },
            {
                targets: [6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {   
                    let buttons = '<a href="/hospital/paciente/editar/' + row.id + '/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a rel="delete" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a> ';
                    return buttons;                   
                    
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
    $('#data_list tbody').on('click', 'a[rel="delete"]', function () {
        const tr = $("#data_list").DataTable().cell($(this).parents('td, li')).index();
        const data = $("#data_list").DataTable().row(tr.row).data();
        let parameters = new FormData();
        parameters.append('action', 'delete');
        parameters.append('id', data.id);
       
        const url = window.location.pathname;
        submit_with_ajax(url, 'Notificación', '¿Estas seguro de eliminar al paciente ' + '<b style="color: #304ffe;">' +  data.full_name + ' / ' + data.cedula + '</b>?', parameters, function () {
            sweet_info( 'El registro ha sido eliminado con exito');
            data_list.row(tr.row).remove().draw();
        });
    });
});