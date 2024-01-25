<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use HasFactory;

    protected $fillable =['id','product_type_id', 'brand_id', 'model', 'description','total_cyclinder_id',
    'hp_category','brake_type_id','warranty','starting_price','ending_price','engine_capacity_cc',
    'engine_rated_rpm','cooling_id','air_filter_id','fuel_pump_id','torque','transmission_type_id','transmission_clutch_id',
    'gear_box_forward','gear_box_reverse','min_forward_speed','max_forward_speed','min_reverse_speed',
    'max_reverse_speed','steering_details_id','steering_column_id','power_take_off_type',
    'power_take_off_rpm','total_weight','wheel_base','lifting_capacity','linkage_point_id','wheel_drive_id',
    'front_tyre','rear_tyre','status_id','additional_feature'];

    public function tractorType()
    {
        return $this->hasMany(Lookup_data::class,'id', 'tractor_type_id');
    }
}
