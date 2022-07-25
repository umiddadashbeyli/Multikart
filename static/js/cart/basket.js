let updateBtns = document.getElementById('update-cart')

updateBtns.addEventListener('click', async function(event){
    event.preventDefault()
    let productId = this.dataset.product
    let action = this.dataset.action
    let userID = this.dataset.user
    let quantity = document.getElementById('quantity').value
    console.log('productID:' , productId, 'action:' , action)
    console.log('User:' , user)

    if (user === 'Anonymous user'){
        window.alert('Not logged in')
    }
    else{
        createBasket(userID)
        createBasketItem(productId, action, quantity)
    }
})

function createBasket(userID){
    let url = '/en/api/basket/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'userID': userID,}),
    })

    .then((response)=>{
        return response.json()
    })
}


function createBasketItem(productID, action, quantity){
    let url = '/en/api/basket_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productID': productID, 'action': action, 'quantity': quantity}),
    })

    .then((response)=>{
        return response.json()
    })
}






