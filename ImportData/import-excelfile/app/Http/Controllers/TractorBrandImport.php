<?php

namespace App\Http\Controllers;
use Excel;
use App\Imports\TractorBrandFile;
use Illuminate\Http\Request;

class TractorBrandImport extends Controller
{
    //
    public function importBrand(Request $request){
       $request->validate([
        'file'=>'required|mimes:xlsx,xls'
       ]);
       $file = $request->file('file');

       //process excel file
       Excel::import(new TractorBrandFile, $file);
       return response()->json('Tractor Brand imported Successfully', 200);
    }
}
