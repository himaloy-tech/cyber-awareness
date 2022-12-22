$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
function bringComments() {
    let postId = document.querySelector('#articleId').value;
    document.querySelector('.comments').innerHTML = '';
    fetch(`/GivemeComment/${postId}`)
        .then(response => response.json())
        .then(comments => {
            comments.forEach(comment => {
                let div = document.createElement('div');
                div.className = 'card';
                div.style.margin = '20px';
                let date = comment.time.split("T");
                let time = date[1].split(".")
                let html = `<div class="card-header">
                ${date[0]} ${time[0]}
          </div>
          <div class="card-body">
            <blockquote class="blockquote mb-0">
              <p>${comment.comment}</p>
            </blockquote>
          </div>`;
                div.innerHTML = html;
                document.querySelector('.comments').append(div);
            })
        })
}
document.addEventListener('DOMContentLoaded', () => {
    bringComments();
    $(document).on('submit', '#form', function (event) {
        event.preventDefault();
        let text = document.querySelector('#text').value;
        let postId = document.querySelector('#articleId').value;
        let data = {
            text: text.toString(),
            articleId: postId.toString(),
        };
        $.ajax({
            type: 'POST',
            url: '/PostComment',
            data: data,
            success: function (json) {
                document.querySelector('#text').value = '';
                bringComments();
                window.scrollTo(0, 0);
            }
        });
        return false;
    })
})