<?php

namespace App\Imports;
use App\Models\Product;
use App\Models\Brand;
use App\Models\Product_type;
use App\Models\Lookup_data;
use App\Models\Lookup_type;
use App\Models\Accessory;
use App\Models\Accessory_mapping;
use App\Models\Images_mapping;
use App\Models\image_types;
use App\Models\Status_type_mappings;
use App\Models\Status_types;
use Illuminate\Support\Collection;
use Maatwebsite\Excel\Concerns\ToCollection;
use Maatwebsite\Excel\Concerns\ToModel;


class TractorDetailsFile implements ToModel
{
    /**
    * @param Collection $collection
    */
    public function model(array $row)
    {
        $r=explode('+',$row[7]);
        $gear_box_forward=explode('Forward', $r[0]);
        $gear_box_reverse=explode('Reverse', $r[1]);
        

        $product = Product::create([
            'brand_id'=>Brand::where('brand_name', $row[0])->first()->id,
            'product_type_id'=>$row[14] !=''?Status_types::where('type_name', $row[14])->first()->id:NULL,
            'model'=>$row[1],
            'description'=>$row[9],
            'total_cyclinder_id'=>$row[5],
            'hp_category'=>$row[4],
            'brake_type_id'=>$row[10]!=''?Lookup_data::where('lookup_data_value', $row[10])->first()->id:NULL,
            'warranty'=>$row[13],
            'starting_price'=>$row[11],
            'ending_price'=>$row[12],
            'engine_capacity_cc'=>$row[15],
            'engine_rated_rpm'=>$row[16],
            'cooling_id'=>$row[17]!=''?Lookup_data::where('lookup_data_value', $row[17])->first()->id:NULL,
            'air_filter_id'=>$row[18]!=''?Lookup_data::where('lookup_data_value', $row[18])->first()->id:NULL,
            'fuel_pump_id'=>$row[19]!=''?Lookup_data::where('lookup_data_value', $row[19])->first()->id:NULL,
            'torque'=>$row[20],
            'transmission_type_id'=> $row[21] !=''?Lookup_data::where('lookup_data_value', $row[21])->first()->id:NULL,
            'transmission_clutch_id'=>$row[22]!=''?Lookup_data::where('lookup_data_value', $row[22])->first()->id:NULL,
            'gear_box_forward'=>$gear_box_forward[0],
            'gear_box_reverse'=>$gear_box_reverse[0],
            'min_forward_speed'=> $row[26]!=''?explode('-', $row[26])[0]:NULL,
            'max_forward_speed'=> $row[26]!=''?explode('-', $row[26])[1]:NULL,
            'min_reverse_speed'=> $row[27]!=''?explode('-', $row[27])[0]:NULL,
            'max_reverse_speed'=> $row[26]!=''?explode('-', $row[26])[1]:NULL,

            'steering_details_id'=> $row[28]!=''?Lookup_data::where('lookup_data_value', $row[28])->first()->id:NULL,
            'steering_column_id'=>$row[29]!=''?Lookup_data::where('lookup_data_value', $row[29])->first()->id:NULL,
            'power_take_off_type'=>$row[30],
            'power_take_off_rpm'=>$row[31],
            'total_weight'=>$row[32],
            'wheel_base'=>$row[33],
            'lifting_capacity'=>$row[38],
            'linkage_point_id'=>$row[39]!=''?Lookup_data::where('lookup_data_value', $row[39])->first()->id:NULL,
            'wheel_drive_id'=>$row[40]!=''?Lookup_data::where('lookup_data_value',$row[40])->first()->id:NULL,
            'front_tyre'=> $row[41],
            'rear_tyre'=> $row[42],
            'status_id'=>$row[46]!=''?Lookup_data::where('lookup_data_value',$row[46])->first()->id:NULL,
            'additional_feature'=>$row[44]
        ]);

        if($row[14] !=''){
            $statustypemap =  Status_type_mappings::create([
                'product_type_id'=>$product->id,
                'status_type_id'=>Status_types::where('type_name', $row[14])->first()->id
            ]); 
        }

        if($row[43] !=''){
            $accessories =  Accessory_mapping::create([
                'product_id'=>$product->id,
                'accessory_id'=>Accessory::where('accessory', $row[43])->first()->id
            ]);
        }

        foreach(explode(',',$row[2]) as $p){
            $imagemapping = Images_mapping::create([
                'product_id'=> $product->id,
                'image_type_id'=>image_types::where('image_type_name', $row[3])->first()->id,
                'image_name'=>$p
            ]);
        }
    }
}
