import Navbar from './../../compnent/Navbar/index';

import { useSelector } from 'react-redux';
import SimpleMenu from './../../compnent/MenuItems/index';
import LODER from './../../compnent/Loder/index';


const Layout=(props)=>{
    const TOKEN=useSelector(({Token})=>Token)
    const TYPE=useSelector(({Type})=>Type)
    return(
        <>
        <LODER/>
        <Navbar/>
        {TYPE==='shopkeper' && TOKEN.length>0?<SimpleMenu/>:null}
        {props.children}
        </>
    )
}
export default Layout
