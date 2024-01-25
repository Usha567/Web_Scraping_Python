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
        $brand = Brand::create([
            'brand_name'=>$row[0],
            'brand_img'=>$row[1]
        ]);

        $brand_type = Brand_type_mapping::create([
            'brand_id'=> $brand->id,
            'product_type_id'=>Product_type::where('product_type_name', $row[2])->first()->id
        ]);
    }
}
