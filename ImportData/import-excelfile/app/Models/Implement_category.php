<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Implement_category extends Model
{
    use HasFactory;
    protected $fillable=['id','category_name'];
}
