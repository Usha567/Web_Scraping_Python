<?php

namespace App\Http\Controllers;
use App\Imports\ExcelFileImport;
use Illuminate\Http\Request;
use Excel;

class ExcelImportController extends Controller
{
    //
    public function import(Request $request)
    {
        //validate import file
        $request->validate([
           'file'=>'required|mimes:xlsx, xls'
        ]);

        $file = $request->file('file');

        //process the excel file
        Excel::import(new ExcelFileImport, $file);
        return response()->json('Excel File imported successfully.', 200);
    }
}
