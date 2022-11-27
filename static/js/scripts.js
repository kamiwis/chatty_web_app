function getDateTime() {
    var now = new Date(); 
    var year = now.getFullYear();
    var month = now.getMonth()+1; 
    var day = now.getDate();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds(); 
    
    if (month.toString().length == 1) {
         month = '0'+month;
    }
    if (day.toString().length == 1) {
         day = '0'+day;
    }   
    if (hour.toString().length == 1) {
         hour = '0'+hour;
    }
    if (minute.toString().length == 1) {
         minute = '0'+minute;
    }
    if (second.toString().length == 1) {
         second = '0'+second;
    }   
    var dateTime = year + '/' + month + '/' + day + ' ' + hour + ':' + minute;   
    return dateTime;
}

$(document).ready(function() {

    var socket = io.connect("http://" + document.domain + ":" + location.port);

        socket.on("connect", function () {
            socket.emit('my event', {
                data: loginName + ' Connected'
            });
    });

    socket.on('my response', function(msg) {
        if ( typeof msg.name !== "undefined" ) {
            var timestamp = getDateTime()
            if (msg.name === loginName) {
                var message = `<div id='right'><p><b>${msg.name}</b>: ${msg.message}</p><span id='date-right'>${timestamp}</span></div>`;
            } else {
                var message = `<div id='left'><p><b>${msg.name}</b>: ${msg.message}</p><span id='date-right'>${timestamp}</span></div>`;
            }
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
});
