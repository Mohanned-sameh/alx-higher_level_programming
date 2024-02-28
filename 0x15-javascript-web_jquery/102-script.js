$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/hello/?';
  $('INPUT#btn_translate').click(function () {
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
  });
});
