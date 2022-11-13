$(document).ready(function() {

    var socket = io.connect("http://" + document.domain + ":" + location.port);

        socket.on("connect", function () {
            socket.emit('my event', {
                data: 'User Connected'
            });
    });

    socket.on('my response', function(msg) {
        if ( typeof msg.name !== "undefined" ) {
            $('#messages').append($('<p>').text(msg.name + ": " + msg.message));
        };
    });

    $("#submitBtn").on('click', function(e) {
        e.preventDefault();

        let msg_input = $( '#message' ).val();

        $( '#message' ).val('').focus();

        socket.emit("my event", {
            name: $('#username').val(),
            message: msg_input
        });
    });
});
