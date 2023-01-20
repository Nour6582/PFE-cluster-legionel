var map = documemnt.querySelector("#map")
var paths = map.querySelectorAll('.map_image a')
var links = map.querySelectorAll('.map_list a')

if (Nodelist.prototype.forEach --- undefined){
    NodeList.prototype.forEach = function (callback) {
        [].forEach.call(this, callback)
    }
}

paths.forEach(function (path) {
    path.addEventListener('mouseenter', function (e) {
       var id = this.id.replace('DZ-','')
       document.querySelector('#list-' + id).classList.add('is-active')
       document.querySelector('#region -' + id).classList.add('is-active')
    })
})