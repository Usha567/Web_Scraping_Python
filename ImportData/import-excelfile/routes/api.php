<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ExcelImportController;
use App\Http\Controllers\TractorBrandImport;
use App\Http\Controllers\ImportTractorDetails;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/
Route:: post('/import-excel',[ExcelImportController::class, 'import']);
// Route::middleware('auth:sanctum')->group( function () {
//     // return $request->user();
// });
Route::post('/import-brand', [TractorBrandImport::class, 'importBrand']);
Route::post('/import-tractor', [ImportTractorDetails::class, 'importTractor']);
Route::post('/import-harvester', [ImportTractorDetails::class, 'importHarvester']);
Route::post('/import-tyre', [ImportTractorDetails::class, 'importTyre']);
Route::post('/import-state-dist', [ImportTractorDetails::class, 'importStateDist']);
Route::post('/import-farm-implement',[ImportTractorDetails::class, 'importFarmImplement']);