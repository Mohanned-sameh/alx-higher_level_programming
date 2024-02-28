$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate() {
  const url = 'https://hellosalut.stefanbohacek.dev/hello/?';
  $.ajax({
    url: url + $.param({ lang: $('INPUT#language_code').val() }),
    success: function (data) {
      $('DIV#hello').text(data.hello);
    },
    error: function (error) {
      console.log(error);
    },
    type: 'GET',
    dataType: 'json',
    crossOriginIsolated: true,
  });
}
