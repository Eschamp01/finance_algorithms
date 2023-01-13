const modelParamsContainer = document.querySelector('#paramsContainer');
const modelChoice = document.querySelector('.dropdown-item');

function modelParameters(model_name){
    if (model_name === "moving average") {
        return (
            `
            <h5 class="text-center">Set Model Parameters</h5>

            <div class="form-group row text-center justify-content-center">
                <div class="col-3">
                    <label for="ma-1">Short MA</label>
                    <input value="20" type="number" id="ma-1" class="form-control">
                </div>
                <div class="col-3">
                    <label for="ma-1">Long MA</label>
                    <input value="40" type="number" id="ma-1" class="form-control">
                </div>
            </div>
            `
        )
    } else {
        return (
            `
            <p>This model type isn't implemented yet. Please leave us a message describing why you would like this implemented!</p>
            <div class="form-group">
                <textarea class="form-control" id="model_feedback" rows="4"></textarea>
                <div style="height:10px"></div>
                <button type="button" class="btn btn-outline-secondary float-end">Submit Feedback</button>
            </div>
            <div style="height:30px"></div>
            `
        )
    }
}

const handleModel = async (model_name) => {
    modelParamsContainer.innerHTML += modelParameters(model_name);
    console.log('model choice pressed');
}

modelChoice.addEventListener('mouseup', handleModel("movin average"));