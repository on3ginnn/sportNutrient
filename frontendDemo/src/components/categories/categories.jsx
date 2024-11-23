import { Container } from "react-bootstrap"
import axios from "axios"
import { useEffect, useState } from "react"
import CategoryItem from "./category_item";
const Categories = ()=>{
    const [data,setData] = useState([]);
    useEffect(()=>{
        async function readData(){
            await axios.get('/api/category/read')
            .then(res=>{
                console.log(res);
                setData(res.data.categories);
            })
            .catch(err=>console.log(err));
        }
        readData();
    },[]);
    return(
        <Container>
            {
                data.map((el,i)=><CategoryItem name={el.name} id={el._id} key={i}/>)
            }
        </Container>
    )
}
export default Categories;