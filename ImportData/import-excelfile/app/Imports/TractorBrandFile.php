<?php

namespace App\Imports;

use App\Models\Brand;
use App\Models\Brand_type_mapping;
use App\Models\Product_type;
use Illuminate\Support\Collection;
use Maatwebsite\Excel\Concerns\ToCollection;
use Maatwebsite\Excel\Concerns\ToModel;
use Illuminate\Http\Request;

class TractorBrandFile implements ToModel
{
    /**
    * @param Collection $collection
    */
    public function model(array $row)
    {
        // $brand = Brand::create([
        //     'brand_name'=>$row[0],
        //     'brand_img'=>$row[1]
        // ]);
        echo '$row[0]-'.$row[0];
        $brands = Brand::where('brand_name', $row[0])->first();
        if(!is_null($brands)){
            echo 'not null';
            $brands->update(['brand_img' => $row[1]]);
            $brands->brand_img = $row[1];
        }
        else{
            echo'null';
            $brand = Brand::create([
                'brand_name'=>$row[0],
                'brand_img'=>$row[1]
            ]);
        }
       

        // $brand = Brand::all()
        echo ' $row[0]-'. $row[0];
        $brand_type = Brand_type_mapping::create([
            'brand_id'=> Brand::where('brand_name', $row[0])->first()->id,
            'product_type_id'=>Product_type::where('product_type_name', $row[2])->first()->id
        ]);
    }
}
