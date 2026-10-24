import { use, useEffect, useRef, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import { Loader } from './Loader.jsx'
import { CropChart } from './crop_chart.jsx'
import { Sprout,Thermometer,
  Droplets,
  CloudRain,
  
 
  FlaskConical, 
  Gauge,
  Atom,
  Zap,
  Search} from 'lucide-react'
function App() {
const [N,setN]=useState("")
const [P,setP]=useState("")
const [K,setK]=useState("")
const [humd,sethumd]=useState("")
const [temp,settemp]=useState("")
const [rfall,setrfall]=useState("")
const [ph,setph]=useState("")
const [chart_data,setchart_data]=useState([])
const [open,setopen]=useState(true)
const [image,setimage]=useState("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_8CnpltNwJ3fNZSvNF6ciPberICsN7VXB_tOSsU1qSQ&s")
const [loader,setloader]=useState(false)
const [prob,setprob]=useState(false)
const [crop3,setcrop3]=useState(false)
const [Suggest,setSuggest]=useState(true)
const [crop,setcrop]=useState("")
const [confidence,setconfidence]=useState("")
const [msg,setmsg]=useState([])
const[prob_loader,setprob_loader]=useState(false)
const [error,seterror]=useState("")

const bottomref=useRef(null)

useEffect(()=>{
  bottomref.current?.scrollIntoView({
      behavior: "smooth"
    });
},[Suggest,msg,prob_loader,open])


  const search=async()=>{
    setopen(false)
    setloader(true)
    
    const response=await fetch("https://crop-show.onrender.com/api/crop/crop_recommendation",
      {
        method:"POST",
        headers:{
          "content-type":"application/json"
        },
        body:JSON.stringify({
        N:N,
        P:P,
        K:K,
        humidity:humd,
        temperature:temp,
        ph:ph,
        rainfall:rfall

      }),
      }
     
    )
    const res=await response.json()
    console.log("res",res)
    if (res.error){
      seterror(res.error)
    }else{
setcrop(res.crop)
    setconfidence(res.confidence)
    setimage(res.url)
    }
    

    setTimeout(()=>{
      setloader(false)
    },3000);
    

    
    
    
  }
  const search_chart=async()=>{
    
    
    const response=await fetch("https://crop-show.onrender.com/api/crop/prob_chart",
      {
        method:"POST",
        headers:{
          "content-type":"application/json"
        },
        body:JSON.stringify({
        N:N,
        P:P,
        K:K,
        humidity:humd,
        temperature:temp,
        ph:ph,
        rainfall:rfall

      }),
      }
     
    )
    const res=await response.json()
    console.log("res",res)
    setchart_data(res)
    setTimeout(() => {
      setprob(true)
      setprob_loader(false)
    }, 2000);
    
    
  }
  const search_crops=async()=>{
    
    const response=await fetch("https://crop-show.onrender.com/api/crop/Top_3_crops",
      {
        method:"POST",
        headers:{
          "content-type":"application/json"
        },
        body:JSON.stringify({
        N:N,
        P:P,
        K:K,
        humidity:humd,
        temperature:temp,
        ph:ph,
        rainfall:rfall

      }),
      }
     
    )
    const res=await response.json()
    console.log("res",res)
   
  }
  const search_suggestion=async()=>{
    
    
    const response=await fetch("https://crop-show.onrender.com/api/crop/fertilizer_suggestion",
      {
        method:"POST",
        headers:{
          "content-type":"application/json"
        },
        body:JSON.stringify({
        N:N,
        P:P,
        K:K,
        

      }),
      }
     
    )
    const res=await response.json()
    console.log("res",res)
    const dat=res.map((item)=>item.msg)
    console.log(dat)
    setmsg(res.map((item)=>item.msg))
    setSuggest(false)

    
    

    }
   
  

  return (
   <>
<div className="min-h-screen bg-green-200 p-10">

   <div  class="w-full  bg-white/90 backdrop-blur-md rounded-3xl border border-white/60 shadow-2xl p-6 md:p-10 flex flex-col gap-8 flex justify-center items-center">
        
        
        <header class="text-center flex flex-col items-center gap-2">
            <div class="inline-flex items-center gap-2 bg-green-100 text-agri-800 px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider border border-green-200">
                <Sprout size={30} color='green' /> Smart Agriculture
            </div>
            <h1 class="text-3xl md:text-4xl font-extrabold text-green-900 tracking-tight">CropShow</h1>
            <p class="text-slate-600 text-sm md:text-base max-w-md">Input your soil and climate indicators below to get instant crop recommendation analysis.</p>
        </header>

       
        <form id="cropForm" onsubmit="event.preventDefault(); handlePredict();" class="space-y-2">
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-5">
                
                
                <div class="flex flex-col gap-1.5">
                    <label for="nitrogen" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                        <FlaskConical size={20} color='green'/>Nitrogen (N)
                    </label>
                    <input
                    
                    value={N}
                    readOnly={!open}
                    onChange={(e)=>{
                      setN(e.target.value)
                    }}
                    type="number" id="nitrogen" step="any" placeholder="e.g. 90" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                
                </div>

                
                <div class="flex flex-col gap-1.5">
                    <label for="phosphorus" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                        <Atom size={20} color='green'/> Phosphorus (P)
                    </label>
                    <input
                    value={P}
                    readOnly={!open}
                    onChange={(e)=>{
                      setP(e.target.value)
                    }}
                    type="number" id="phosphorus" step="any" placeholder="e.g. 42" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>

                
                <div class="flex flex-col gap-1.5">
                    <label for="potassium" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                       <Zap size={20} color='green'/> Potassium (K)
                    </label>
                    <input
                    value={K}
                    readOnly={!open}
                    onChange={(e)=>{
                      setK(e.target.value)
                    }}
                    type="number" id="potassium" step="any" placeholder="e.g. 43" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>

                
                <div class="flex flex-col gap-1.5">
                    <label for="ph" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                        <Gauge size={20} color='green'/> Soil pH
                    </label>
                    <input
                    value={ph}
                    readOnly={!open}
                    onChange={(e)=>{
                      setph(e.target.value)
                    }}
                    type="number" id="ph" step="1" min="0" max="14" placeholder="e.g. 6.5" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>

                
                <div class="flex flex-col gap-1.5">
                    <label for="temperature" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                       <Thermometer size={20} color='green'/> Temp (°C)
                    </label>
                    <input
                    value={temp}
                    readOnly={!open}
                    onChange={(e)=>{
                      settemp(e.target.value)
                    }}
                    type="number" id="temperature" step="1" placeholder="e.g. 20.8" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>

                
                <div class="flex flex-col gap-1.5">
                    <label for="humidity" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                        <Droplets size={20} color='green'/> Humidity (%)
                    </label>
                    <input
                    readOnly={!open}
                    value={humd}
                    onChange={(e)=>{
                      sethumd(e.target.value)
                    }}
                    type="number" id="humidity" step="1" min="0" max="100" placeholder="e.g. 82.0" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>

               
                <div class="flex flex-col gap-0 sm:col-span-2 md:col-span-3">
                    <label for="rainfall" class="text-xs font-semibold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                        <CloudRain size={20} color='green'/> Rainfall (mm)
                    </label>
                    <input
                    readOnly={!open}
                    value={rfall}
                    onChange={(e)=>{
                      setrfall(e.target.value)
                    }}
                    type="number" id="rainfall" step="1" placeholder="e.g. 202.9" required
                        class="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-white/80 text-sm focus:outline-none focus:ring-2 focus:ring-agri-700/20 focus:border-agri-700 transition"/>
                </div>
            </div>

            
            <button
            onClick={(e)=>{
              e.preventDefault()
              search()
              
            }}
            type="Submit" 
                class="w-full py-3.5 px-6 bg-green-700 hover:bg-green-800 text-white font-semibold rounded-xl shadow-lg shadow-agri-700/20 hover:shadow-agri-700/30 active:scale-[0.99] transition flex items-center justify-center gap-0 text-base cursor-pointer">
                <span className='text-white mr-3'>Recommend Best Crop</span>  <Search size={20} color='white'/> 
            </button>
        </form>

        
        {open?<></>:<div ref={bottomref} class="p-2 flex flex-col gap-0 w-80 lg:w-4/6  md:w-4/5 sm:w-3/5 sm:h-100 md:h-100 border-4 animate-border-blink rounded-2xl ">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Recommendation Output</span>
            <div id="responseContainer" 
                class={`w-full h-full p-4  rounded-2xl ${error?"flex justify-center items-center bg-slate-200 border border-black":"bg-white"} overflow-y-auto custom-scrollbar text-sm text-slate-700 leading-relaxed shadow-inner`}>
               {loader? <Loader/>:(error? <div className='tex-black font-bold text-lg '>
                <h2>
{error}
                </h2>
                

                
                  <button
                  onClick={()=>{
                    setopen(true)
                    seterror(false)
                  }}
                  className=' p-1 rounded-2xl bg-green-500 text-white text-lg flex justify-center w-full hover:bg-green-700'>
                      Click to reset value
                  </button>
                
               </div> :<div className=' relative'>
                <img 
               class="w-full rounded-2xl border-5 border-slate-400"
               src={image} alt="" />
               <div className='absolute bottom-33 right-5 sm:bottom-30 sm:right-3 lg:bottom-17'>
                    <span 
               className='bg-white m-4 p-2 rounded-2xl font-bold text-black '
               >{crop}</span>
               <span className='font-bold text-black bg-white p-2 rounded-2xl'>{confidence}%</span>

               </div>
               <div className='flex-col'>
                <button
                onClick={(e)=>{
                  e.preventDefault()
                  setprob_loader(!prob_loader)
                  search_chart()
                }}
                className='p-1 bg-black rounded-lg text-white font-bold m-1'>Show Probability Chart</button>
                <button
                onClick={(e)=>{
                  e.preventDefault()
                  search_suggestion()
                  
                }}
                className='p-1 bg-black rounded-lg text-white font-bold m-1'>Want Fertilizer Suggestion?</button>
                <button className='p-1 bg-black rounded-lg text-white font-bold m-1'>Top 3 Crops</button>
                
               </div>
               
               </div>)}

               <div ref={bottomref}>
{prob?<CropChart
               
               res={chart_data}/>:(prob_loader?<Loader/>:<></>)}
               </div>
               
               {Suggest?<></>:
               <div ref={bottomref}>
                {msg.map((msg)=>  <ul key={msg} className='font-bold text-green-500' >{msg}</ul> )}


               </div>
               
          
               }
              
               
               
                {/* <p class="text-slate-400 italic">Submit environmental metrics above to generate a crop analysis report...</p> */}
            </div>
        </div>
}
    </div>
</div>

  
    
   </>
  )
}

export default App
