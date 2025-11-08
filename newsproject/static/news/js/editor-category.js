document.addEventListener('DOMContentLoaded', function() {
   const subcategory_container = document.querySelector(".subcategory-row")
   const subcategory_select = document.querySelector("#articleSubCategory");
   
   const category_select = document.querySelector("#articleCategory");
   subcategory_container.style.display = 'none';
   category_select.addEventListener('change', function(event) {
       const category_item = event.target.options[event.target.selectedIndex].text.toLowerCase();
       for (let i = 0; i < subcategory_select.children.length; i++) {
            subcategory_select.children[i].style.display = 'block';
        }


       for(let i = 0; i < subcategory_select.children.length; i++) {
        let option_arr = subcategory_select.children[i].text.split(" ");      
        let str = option_arr[option_arr.length - 1];
        let clean = str.replace(/[()]/g, "").toLowerCase();
        if (clean != category_item) {
        subcategory_select.children[i].style.display = 'none';
        }
       }
    subcategory_container.style.display = 'flex';
})
    
})