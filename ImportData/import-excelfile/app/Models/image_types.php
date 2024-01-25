<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class image_types extends Model
{
    use HasFactory;
    protected $fillable=['id','image_type_name'];
}
