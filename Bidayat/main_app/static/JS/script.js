window.onload = function () {
  imgs = document.getElementById('slideshow').children
  interval = 4000
  currentPic = 0
  imgs[currentPic].style.webkitAnimation = 'fadey ' + interval + 'ms'
  imgs[currentPic].style.animation = 'fadey ' + interval + 'ms'
  let infiniteLoop = setInterval(function () {
    imgs[currentPic].removeAttribute('style')
    if (currentPic == imgs.length - 1) {
      currentPic = 0
    } else {
      currentPic++
    }
    imgs[currentPic].style.webkitAnimation = 'fadey ' + interval + 'ms'
    imgs[currentPic].style.animation = 'fadey ' + interval + 'ms'
  }, interval)
}
