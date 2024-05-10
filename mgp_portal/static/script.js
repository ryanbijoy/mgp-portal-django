window.onload = function () {
  var startPos;
  var geoSuccess = function (position) {
    startPos = position;
    document.getElementById("id_latitude").value = position.coords.latitude
    document.getElementById("id_longitude").value = position.coords.longitude

  };
  navigator.geolocation.getCurrentPosition(geoSuccess);
};
