let currentIndex = 0;
const items = document.querySelectorAll('.item');  // Lấy tất cả các phần tử có class "item"
const slideInterval = 3000;  // Thời gian giữa các slide (tính bằng ms), ở đây là 3 giây

let next = document.querySelector('.next')
let prev = document.querySelector('.prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').appendChild(items[0])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1]) // here the length of items = 6
})

// Tự động chuyển slide sau mỗi khoảng thời gian đã định
setInterval(nextSlide, slideInterval);