<?php

namespace App\Imports;

use App\Models\Product;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Tyre_category;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Images_mapping;
use App\Models\image_types;
use Maatwebsite\Excel\Concerns\ToModel;

class TyreDetailsFile implements ToCollection
{
    /**
    * @param array $row
    *
    * @return \Illuminate\Database\Eloquent\Model|null
    */
    public function model(array $row)
    {
        //For checking error
        // echo '$row[10]-'.$row[10] . "\n";
        // if($row[10]!=''){
        //     $id=Status_types::where('type_name', $row[10])->first()->id;
        //     echo 'id-'.$id;
        // }
        // else{
        //     echo 'else\n';
        //     null;
        // }

        echo '$row[0]-'.$row[0];
        $product = Product::create([
            'brand_id'=>$row[0] !=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL,
            'product_type_id'=>$row[9] !=''?Product_type::where('product_type_name', trim($row[9]))->first()->id:NULL,
            'model'=>$row[1],
            'description'=>json_encode($row[7]),
            'implement_category_id'=>$row[3]!=''?Tyre_category::where('category', trim($row[3]))->first()->id:NULL,
            'tyre_position'=>$row[4]!=''?$row[4]:NULL,
            'tyre_diameter'=>$row[5]!=''?$row[5]:NULL,
            'tyre_width'=>$row[6]!=''?$row[6]:NULL,
        ]);
        
        #Need to play with image here
        echo '$row[1]-'.$row[1];
        $prod = Product::where('model', $row[1])->first();
        if(!is_null($prod)){
            $prod_id= $prod->id;
            $imagemapping = Images_mapping::create([
                'product_id'=>  $prod_id,
                'image_type_id'=>image_types::where('image_type_name', trim($row[8]))->first()->id,
                'image_name'=>trim($row[2])
            ]);
        }
        else{
            echo 'prod null';
        }
    }
}
