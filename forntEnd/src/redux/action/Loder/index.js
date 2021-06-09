import { LODER } from "../../actionTypes";

const LoderOperation={
    show:()=>dispatch=>{
        dispatch({
            type:LODER.showLoder
        })
    },
    hide:()=>dispatch=>{
        dispatch({
            type:LODER.hideLoder
        })
    }
}

export default LoderOperation