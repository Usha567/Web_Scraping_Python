<?php

namespace App\Imports;

use App\Models\Product;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Images_mapping;
use App\Models\image_types;
use Maatwebsite\Excel\Concerns\ToModel;

class HarvesterDetailsFile implements ToModel
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

        echo '$row[29]-'.$row[29];
        if($row[29] != ''){
            $r=explode('+',$row[29]);
            $gear_box_forward=$r[0];
            $gear_box_reverse=$r[1];
        }
        else{
            $gear_box_forward=[''];
            $gear_box_reverse=[''];
        }

        echo '$row[3]-'.$row[3];
        $product = Product::create([
            'brand_id'=>$row[0] !=''?Brand::where('brand_name', trim($row[0]))->first()->id:NULL,
            'product_type_id'=>$row[40] !=''?Product_type::where('product_type_name', $row[40])->first()->id:NULL,
            'model'=>$row[1],
            'total_cyclinder_id'=>$row[4]!=''?Lookup_data::where('lookup_data_value', $row[4])->first()->id:NULL,
            'hp_category'=>$row[9]!=''?$row[9]:NULL,
            'engine_rated_rpm'=>$row[8],
            'air_filter_id'=>$row[11]!=''?Lookup_data::where('lookup_data_value', trim($row[11]))->first()->id:NULL,
            'power_source_id'=>$row[5]!=''?Lookup_data::where('lookup_data_value', trim($row[5]))->first()->id:NULL,
            'cutting_bar_width'=>$row[3],
            'min_cutting_height'=>$row[12],
            'max_cutting_height'=>$row[13],
            'cutter_bar_height_adjustment_id'=>$row[14]!=''?Lookup_data::where('lookup_data_value', trim($row[14]))->first()->id:NULL,
            
            'reel_type_id'=>$row[15]!=''?Lookup_data::where('lookup_data_value', trim($row[15]))->first()->id:NULL,
            'reel_diameter'=>$row[16],
            'speed_adjustment_id'=>$row[17]!=''?Lookup_data::where('lookup_data_value', trim($row[17]))->first()->id:NULL,
            'reel_height_adjustment_id'=>$row[20]!=''?Lookup_data::where('lookup_data_value', trim($row[20]))->first()->id:NULL,
            'min_reel_revolution'=>$row[19],
            'max_reel_revolution'=>$row[18],
            'cooling_id'=>$row[21]!=''?Lookup_data::where('lookup_data_value', trim($row[21]))->first()->id:NULL,
            'coolant_capacity'=>$row[22],

            'threshing_drum_width'=>$row[23],
            'threshing_drum_length'=>$row[24],
            'threshing_drum_diameter'=>$row[25],
            'threshing_drum_speed_adjustment_id'=>$row[26]!=''?Lookup_data::where('lookup_data_value', trim($row[26]))->first()->id:NULL,
            'clearance_concave'=>$row[27],

            'grain_tank_capacity'=>$row[28],
            'transmission_forward' =>$gear_box_forward,
            'transmission_reverse'=>$gear_box_reverse,
            'clutch_type_id'=> $row[30]!=''?Lookup_data::where('lookup_data_value', trim($row[30]))->first()->id:NULL,
            'front_tyre'=> $row[31],
            'rear_tyre'=> $row[32],
            'total_weight_without_grains'=> $row[34],
            'dimension_length'=> $row[35],
            'dimension_width'=>$row[36],
            'dimension_height'=>$row[37],
            'ground_clearance'=>$row[38],
            'crops_type_id'=>$row[6]!=''?Lookup_data::where('lookup_data_value',trim($row[6]))->first()->id:NULL,
        ]);
        
        #Need to play with image here
        echo '$row[1]-'.$row[1];
        $prod = Product::where('model', $row[1])->first();
        if(!is_null($prod)){
            $prod_id= $prod->id;
            $imagemapping = Images_mapping::create([
                'product_id'=>  $prod_id,
                'image_type_id'=>image_types::where('image_type_name', trim($row[39]))->first()->id,
                'image_name'=>trim($row[2])
            ]);
        }
        else{
            echo 'prod null';
        }
    }
}
