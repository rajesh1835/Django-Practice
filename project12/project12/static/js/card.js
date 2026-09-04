let like;
let dislike;

if (localStorage.getItem("like")) {
  like = Number(localStorage.getItem("like"));
} else {
  like = 0;
}
let likes = document.getElementById("like-ele");
likes.textContent = like;

if (localStorage.getItem("dislike")) {
  dislike = Number(localStorage.getItem("dislike"));
} else {
  dislike = 0;
}
let dislikes = document.getElementById("dislike-ele");
dislikes.textContent = dislike;

let total = document.getElementById("total-ele");
total.textContent = like + dislike;

function likeCount() {
  like = like + 1;
  likes.textContent = like;
  total.textContent = like + dislike;
  localStorage.setItem("like", like);
}

function dislikeCount() {
  dislike = dislike + 1;
  dislikes.textContent = dislike;
  total.textContent = like + dislike;
  localStorage.setItem("dislike", dislike);
}

let likeBtn = document.getElementById("like-btn");
likeBtn.addEventListener("click", likeCount);
let dislikeBtn = document.getElementById("dislike-btn");
dislikeBtn.addEventListener("click", dislikeCount);
