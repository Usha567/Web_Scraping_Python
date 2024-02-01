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
        if(str_contains($row[29], '+')){
            $r=explode('+',$row[29]);
            $gear_box_forward=(explode('Forward', $r[0]))[0];
            $gear_box_reverse=(explode('Reverse', $r[1]))[0];
        }
        else{
            $half_gear=$row[29]/2;
            $gear_box_forward=$half_gear;
            $gear_box_reverse=$half_gear;
        }
        // need to discuss for air filter also
        $product = Product::create([
            'brand_id'=>Brand::where('brand_name', $row[0])->first()->id,
            'model'=>$row[1],
            'engine_rated_rpm'=>$row[9],
            'hp_category'=>$row[10]!='' && $row[10]!='N/A'?explode('HP', $row[3])[0]:NULL,
            'air_filter_id'=>$row[11]!=''?Lookup_data::where('lookup_data_value', $row[11])->first()->id:NULL,
            'total_cyclinder_id'=>$row[4],
            'power_source_id'=>$row[5]!=''?Lookup_data::where('lookup_data_value', $row[5])->first()->id:NULL,
            'cutting_bar_width'=>$row[3],
            'max_cutting_height'=>$row[13],
            'min_cutting_height'=>$row[12],
            'cutter_bar_height_adjustment_id'=>$row[14]!=''?Lookup_data::where('lookup_data_value', $row[14])->first()->id:NULL,
            'reel_type_id'=>$row[15]!=''?Lookup_data::where('lookup_data_value', $row[15])->first()->id:NULL,
            'reel_diameter'=>$row[16],
            'speed_adjustment_id'=>$row[17]!=''?Lookup_data::where('lookup_data_value', $row[17])->first()->id:NULL,
            'min_reel_revolution'=>$row[19],
            'max_reel_revolution'=>$row[18],
            'reel_height_adjustment_id'=>$row[20]!=''?Lookup_data::where('lookup_data_value', $row[20])->first()->id:NULL,
            'cooling_id'=>$row[21]!=''?Lookup_data::where('lookup_data_value', $row[21])->first()->id:NULL,
            'coolant_capacity'=>$row[22], 
            'threshing_drum_width'=>$row[23], 
            'threshing_drum_length'=>$row[24], 
            'threshing_drum_diameter'=>$row[25],
            'threshing_drum_speed_adjustment_id'=>$row[26]!=''?Lookup_data::where('lookup_data_value', $row[26])->first()->id:NULL,
            'clearance_concave'=>$row[27],
            'grain_tank_capacity'=>$row[28],
            'transmission_forward'=>$gear_box_forward,
            'transmission_reverse'=>$gear_box_reverse,
            'clutch_type_id'=>$row[30]!=''?Lookup_data::where('lookup_data_value', $row[30])->first()->id:NULL,
            'front_tyre'=> $row[31],
            'rear_tyre'=> $row[32],
            'total_weight_without_grains'=>$row[34],
            'dimension_length'=> $row[35],
            'dimension_height'=> $row[36],
            'dimension_width'=>$row[37],
            'ground_clearance'=>$row[38],
            'crops_type_id'=>$row[6]!=''?Lookup_data::where('lookup_data_value', $row[6])->first()->id:NULL
        ]);

        foreach(explode(',',$row[2]) as $p){
            $imagemapping = Images_mapping::create([
                'product_id'=> $product->id,
                'image_type_id'=>image_types::where('image_type_name', $row[39])->first()->id,
                'image_name'=>$p
            ]);
        }
    }
}
