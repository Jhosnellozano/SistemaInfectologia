$(function () {
  const today = moment().format("YYYY-MM-DD");

  $("#fecha").datetimepicker({
    format: "YYYY-MM-DD",
    locale: "es",
    minDate: today, // Deshabilita las fechas anteriores a hoy
    icons: {
      time: "fa fa-clock",
      date: "fa fa-calendar",
      up: "fa fa-arrow-up",
      down: "fa fa-arrow-down",
      previous: "fa fa-chevron-left",
      next: "fa fa-chevron-right",
      today: "fa fa-calendar-check-o",
      clear: "fa fa-trash",
      close: "fa fa-times",
    },
  });
  $("#hora").datetimepicker({
    format: "HH:mm",
    step: 30,
    locale: "es",
    useCurrent: false, // Evitar que se seleccione la hora actual por defecto
    icons: {
      time: "fa fa-clock",
      up: "fa fa-arrow-up",
      down: "fa fa-arrow-down",
    },
  });

  $(".select2").select2({
    theme: "bootstrap4",
    language: "es",
  });
});
