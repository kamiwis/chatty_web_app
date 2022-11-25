$(document).ready(function() {

    var socket = io.connect("http://" + document.domain + ":" + location.port);

        socket.on("connect", function () {
            socket.emit('my event', {
                data: loginName + ' Connected'
            });
    });

    socket.on('my response', function(msg) {
        if ( typeof msg.name !== "undefined" ) {
            var message = $('<p>').text(msg.name + ": " + msg.message)
            $('#messages').append(message);
            $('#messages').scrollTop($("#messages").height());
        };
    });

    $("#submitBtn").on('click', function(e) {
        e.preventDefault();

        let msg_input = $( '#message' ).val();

        $( '#message' ).val('').focus();

        socket.emit("my event", {
            name: loginName,
            message: msg_input
        });
    });

    // if (scroll) {
    //     autoScrollToBottom("messsges");
    // };

    // function autoScrollToBottom(id) {
    //     var messagesDiv = document.getElementById(id);
    //     $("#" + id).animate({
    //         scrollTop: messagesDiv.scrollHeight - messagesDiv.clientHeight,
    //     }, 500);
    // };
});
