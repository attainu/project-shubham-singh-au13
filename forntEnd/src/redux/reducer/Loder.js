import { LODER } from "../actionTypes"
const initialState=false
const Loder=(state,action)=>{
    state=state||initialState
    switch(action.type){
        case LODER.showLoder:
            return true
        case LODER.hideLoder:
            return false
        default:
            return state
    }
}
export default Loder