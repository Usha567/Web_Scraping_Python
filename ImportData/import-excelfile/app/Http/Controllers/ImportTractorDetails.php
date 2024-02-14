<?php

namespace App\Http\Controllers;
use Excel;
use App\Imports\TractorDetailsFile;
use App\Imports\HarvesterDetailsFile;
use App\Imports\TyreDetailsFile;
use App\Imports\StateDistFile;
use Illuminate\Http\Request;

class ImportTractorDetails extends Controller
{
    //
    public function importTractor(Request $request){
        $request->validate([
         'file'=>'required|mimes:xlsx,xls'
        ]);
        $file = $request->file('file');
        echo '$file--'. $file;
 
        //process excel file
        try{
            echo 'try';
            Excel::import(new TractorDetailsFile, $file);
        }
        catch(Exception $e){
            echo 'exception-'.$e;
        }
       
        return response()->json('Tractor details imported Successfully', 200);
    }
    public function importHarvester(Request $request){
        $request->validate([
            'file'=>'required|mimes:xlsx,xls'
        ]);
        $file = $request->file('file');

        try{
            Excel::import(new HarvesterDetailsFile , $file);
        }
        catch(Exception $e){
            echo 'exception-'.$e;
        }
        
       
        return response()->json('Harvester details imported Successfully',200);
    }
    public function importTyre(Request $request){
        $request->validate([
            'file'=>'required|mimes:xlsx,xls'
        ]);
        $file = $request->file('file');
        
        Excel::import(new TyreDetailsFile , $file);
        return response()->json('Tyre details imported Successfully',200);
    }
    public function importStateDist(Request $request){
        $request->validate([
            'file'=>'required|mimes:xlsx,xls'
        ]);
        $file = $request->file('file');
        
        Excel::import(new StateDistFile , $file);
        return response()->json('State Dist details imported Successfully',200);
    }
}
