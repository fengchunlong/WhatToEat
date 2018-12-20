Page({
    data:{
        pageStatus: 'loading',
        food : null,
        cookbook : []
    },
    onLoad: function(option){
        this.setData({
          food: option.food,
        })
        this.getCookBook(option.food)
    },
    getCookBook: function(food){
        this.setData({pageStatus: 'loading'})
        var that = this
        wx.request({
            url: 'http://127.0.0.1:5000/api/food/cookbook',
            header: app.getRequestHeader(),
            method: 'POST',
            data: {'food':food},
            success: function (response) {
                console.log(response.data.data)
                that.setData({
                    cookbook: response.data.data,
                    pageStatus: 'done'
                })
            }
        })
    },
    goToIndex: function (){
        wx.switchTab({
            url: "../index/index"
        });
    }
})
