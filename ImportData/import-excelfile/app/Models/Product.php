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
    'front_tyre','rear_tyre','status_id','additional_feature', 'power_source_id','cutting_bar_width', 'min_cutting_height','max_cutting_height', 'cutter_bar_height_adjustment_id',
    'reel_type_id', 'reel_diameter','speed_adjustment_id','reel_height_adjustment_id','min_reel_revolution','max_reel_revolution','cooling_id','coolant_capacity','threshing_drum_width',
    'threshing_drum_length','threshing_drum_diameter','threshing_drum_speed_adjustment_id','clearance_concave',
    'grain_tank_capacity','transmission_forward','transmission_reverse','clutch_type_id','front_tyre','rear_tyre','total_weight_without_grains','dimension_length','dimension_width','dimension_height','ground_clearance',
    'crops_type_id','implement_category_id','tyre_position','tyre_diameter','tyre_width'];

    public function tractorType()
    {
        return $this->hasMany(Lookup_data::class,'id', 'tractor_type_id');
    }
}
