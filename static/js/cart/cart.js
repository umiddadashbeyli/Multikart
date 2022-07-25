window.addEventListener('load', async function(){
    let basket = await fetch('http://127.0.0.1:8000/en/api/basket_item/')
    let basketItems = await basket.json()
    console.log(basketItems)

    for(let basketItem of basketItems){
        let total = basketItem.quantity * basketItem.product.price
        document.getElementById('basketItems').innerHTML += `
        <tr>
            <td>
                <a href="#"><img src="${basketItem.product.main_image}" alt=""></a>
            </td>
            <td><a href="#">${basketItem.product.title}</a>
                <div class="mobile-cart-content row">
                    <div class="col-xs-3">
                        <div class="qty-box">
                            <div class="input-group">
                                <input type="text" name="quantity" class="form-control input-number"
                                    value="1">
                            </div>
                        </div>
                    </div>
                    <div class="col-xs-3">
                        <h2 class="td-color">$63.00</h2>
                    </div>
                    <div class="col-xs-3">
                        <h2 class="td-color"><a href="#" class="icon"><i class="ti-close"></i></a>
                        </h2>
                    </div>
                </div>
            </td>
            <td>
                <h2>${basketItem.product.price}</h2>
            </td>
            <td>
                <div class="qty-box">
                    <div class="input-group">
                        <input type="number" name="quantity" class="form-control input-number"
                            value="${basketItem.quantity}">
                    </div>
                </div>
            </td>
            <td><a href="#" class="icon"><i class="ti-close"></i></a></td>
            <td>
                <h2 class="td-color">${total}</h2>
            </td>
        </tr>
    `
    }



    for(let basketItem of basketItems){
        let total = basketItem.quantity * basketItem.product.price
        document.getElementById('cartsection').innerHTML += `
        <li>
            <div class="media">
                <a href="#"><img class="mr-3"
                        src="${basketItem.product.main_image}"
                        alt="Generic placeholder image"></a>
                <div class="media-body">
                    <a href="#">
                        <h4>${basketItem.product.title}</h4>
                    </a>
                    <h4><span>${basketItem.quantity} x ${basketItem.product.price}</span></h4>
                </div>
            </div>
            <div class="close-circle">
                <a href="#"><i class="fa fa-times" aria-hidden="true"></i></a>
            </div>
        </li>
    `
    }
})





