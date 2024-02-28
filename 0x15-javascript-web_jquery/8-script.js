$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',

  success: function (data) {
    for (const film of data.results) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    }
  },
  error: function (data) {
    console.log('ERROR: ' + data);
  },
});
