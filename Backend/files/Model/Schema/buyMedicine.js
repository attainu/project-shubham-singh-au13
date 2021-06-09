const mongoose=require('mongoose')
const buymedicine=mongoose.Schema({
    buyerId:{
        type:mongoose.Schema.Types.ObjectId,
        ref:'userProfile'
    },
    medicineId:{
        type:mongoose.Schema.type.ObjectId,
        ref:'Addmedicine'
    },
    buy:{
        type:Boolean,
        default:false
    },
    date:{
        type:Date,
        default:Date.now()
    },
    cart:{
        type:Boolean,
        default:false
    },
    quantity:{
        type:Number,
        required:[true,'enter the number of medicine you want to buy']
    }
})

export default mongoose.model('buymedicine',buymedicine)