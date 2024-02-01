<?php

namespace App\Http\Controllers;
use Excel;
use App\Imports\TractorDetailsFile;
use Illuminate\Http\Request;

class ImportTractorDetails extends Controller
{
    //
    public function importTractor(Request $request){
        $request->validate([
         'file'=>'required|mimes:xlsx,xls'
        ]);
        $file = $request->file('file');
 
        //process excel file
        Excel::import(new TractorDetailsFile, $file);
        return response()->json('Tractor details imported Successfully', 200);
    }
    public function importHarvester(Request $request){
        $request->validate([
            'file'=>'required|mimes:xlsx, xls'
        ]);
        $file = $request->file('file');
        
        Excel::import(new HarvesterDetailsFile , $file);
        return response()->json('Harvester details imported Successfully',200);
    }


}
