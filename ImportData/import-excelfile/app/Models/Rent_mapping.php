<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Rent_mapping extends Model
{
    use HasFactory;

    protected $fillable = [
        'customer_id',  // Add this line
        'implement_type_id',
        'rate',
        'rate_per',
        'images',
    ];
}
