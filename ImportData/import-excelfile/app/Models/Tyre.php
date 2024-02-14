<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Tyre extends Model
{
    use HasFactory;
    protected $fillable =['id','brand_id', 'tyre_model', 'tyre_position', 'tyre_size','tyre_category_id'];
}
