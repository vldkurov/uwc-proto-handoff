$(window).on('load', function () {
    function initMap(rawData) {
        const map = new google.maps.Map(document.getElementById("map"), {
            center: {lat: 54.526, lng: -4.248},
            zoom: 6,
        });

        $.each(rawData, function (_, branch) {
            if (branch.latitude && branch.longitude) {
                const marker = new google.maps.Marker({
                    position: {lat: branch.latitude, lng: branch.longitude},
                    map: map,
                    title: branch.title,
                });

                const infoWindow = new google.maps.InfoWindow({
                    content: `
                        <div>
                            <h5>${branch.title}</h5>
                            <p>${branch.address}</p>
                            <p>${branch.postcode || ''}</p>
                            <p>${branch.other_details || ""}</p>
                        </div>
                    `,
                });

                marker.addListener("click", function () {
                    infoWindow.open(map, marker);
                });
            }
        });
    }

    if (window.rawData) {
        initMap(window.rawData);
    }
});