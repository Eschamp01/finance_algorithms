const modelParamsContainer = document.querySelector('#paramsContainer');
const modelSelected = document.querySelector('#model_selected');
var myDropdown = document.querySelector('#model_dropdown')


function modelParameters(model_name){
    model_params_html = `<h5 class="text-center">Set Model Parameters</h5>`
    if (model_name === "moving_average") {
        model_params_html += 
            `
            <div class="form-group row text-center justify-content-center pb-3">
                <div class="col-3">
                    <label for="ma-1">Short MA</label>
                    <input value="20" type="number" id="ma-1" class="form-control">
                </div>
                <div class="col-3">
                    <label for="ma-2">Long MA</label>
                    <input value="40" type="number" id="ma-2" class="form-control">
                </div>
            </div>
            `
            modelSelected.innerHTML = "Moving Average"
    } else if (model_name === "mean_reversion") {
        model_params_html += 
            `
            <div class="form-group row text-center justify-content-center pb-3">
                <div class="col-3">
                    <label for="mr-1">Buy Ratio (low)</label>
                    <input value="0.9" type="number" step="0.1" id="mr-1" class="form-control">
                </div>
                <div class="col-3">
                    <label for="ma-2">Sell Ratio (high)</label>
                    <input value="1.1" type="number" step="0.1" id="mr-2" class="form-control">
                </div>
            </div>
            `
            modelSelected.innerHTML = "Mean Reversion"
    }  else if (model_name === "pairs_trading") {
        model_params_html += 
            `
            <div class="form-group row text-center justify-content-center pb-3">
                <div class="col-3">
                    <label for="stock_selector">Second Stock</label>
                    <select class="form-select" id="stock_selector" aria-label="Default select example">
                        <option selected>Apple (AAPL)</option>
                        <option value="2">Microsoft (MSFT)</option>
                        <option value="3">IBM (IBM)</option>
                    </select>
                </div>
    
                <div class="col-3">
                    <label for="pt-1">Buy ratio (low)</label>
                    <input value="0.9" type="number" step="0.1" id="pt-1" class="form-control">
                </div>

                <div class="col-3">
                    <label for="pt-2">Sell Ratio (high)</label>
                    <input value="1.1" type="number" step="0.1" id="pt-2" class="form-control">
                </div>
            </div>
            `
            modelSelected.innerHTML = "Pairs Trading"
    } else {
        return (
            `
            <p>This model type isn't implemented yet. Please leave us a message describing why you would like this implemented!</p>
            <div class="form-group pb-4">
                <textarea class="form-control" id="model_feedback" rows="4"></textarea>
                <div style="height:10px"></div>
                <button type="button" class="btn btn-outline-secondary float-end">Submit Feedback</button>
            </div>
            `
        )
    }
    model_params_html += ` <div class="text-center"> <button type="button" class="btn btn-outline-secondary text-center">Run Model</button> </div>`
    return model_params_html
}

const handleModel = async (model_name) => {
    modelParamsContainer.innerHTML = modelParameters(model_name);
}

// modelSelected.addEventListener('show.bs.dropdown', function () {
//     console.log('function activated')
//     modelSelected.innerHTML = "Selected"  
// })