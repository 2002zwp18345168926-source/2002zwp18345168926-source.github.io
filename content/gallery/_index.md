+++
title = "相册"
draft = false
+++

## 我和朋友

记录我们一起度过的时光。

<div class="photo-grid">
  <img src="/images/0bd8b1f0676b32c076aab7abf5d4aaf8.jpg" alt="朋友合照 1">
  <img src="/images/23561_livephoto.jpeg" alt="朋友合照 2">
  <img src="/images/51599.jpg" alt="朋友合照 3">
  <img src="/images/IMG_2412.jpeg" alt="朋友合照 4">
  <img src="/images/IMG_5407.jpeg" alt="朋友合照 5">
  <img src="/images/IMG_5421.jpeg" alt="朋友合照 6">
  <img src="/images/IMG_5458.JPG" alt="朋友合照 7">
</div>

<style>
.photo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-top: 20px;
}

.photo-grid img {
  width: 100%;
  height: 280px;
  object-fit: cover;
  border-radius: 10px;
}
</style>