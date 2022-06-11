$(".go").click(
    function (e) {
        let id = this.getAttribute("data-id")
        // console.log(id)
        $.ajax({
            url: "/link/"+id+"/dem"
        })

    }
)